def solution(bandage, health, attacks):
    prev_time = 0
    current_health = health
    
    for time, dmg in attacks:
        elapsed = time - prev_time - 1
        prev_time = time
        
        current_health += (elapsed * bandage[1]) + (elapsed // bandage[0] * bandage[2])
        current_health = min(health, current_health)
        current_health -= dmg
        
        if current_health <= 0:
            return -1
    return current_health