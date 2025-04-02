def min_eating_speed(piles, H):
    def can_eat_all(K):
        total_hours = 0
        for bananas in piles:
            hours = bananas // K
            if bananas % K != 0:
                hours += 1  
            total_hours += hours
        return total_hours <= H

    left = 1  
    right = 0
    for bananas in piles:
        if bananas > right:
            right = bananas  

    while left < right:
        mid = (left + right) // 2
        if can_eat_all(mid):
            right = mid
        else:
            left = mid + 1

    return left