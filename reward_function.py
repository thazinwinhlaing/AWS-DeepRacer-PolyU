def reward_function(params):
    """
    Reward function for AWS DeepRacer to optimize track navigation.
    Encourages staying on track, maintaining speed, and centering.
    """
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    
    # Initialize reward
    reward = 1e-3  # Small base reward to avoid zero
    
    # Penalize if off track
    if not all_wheels_on_track:
        return float(reward)
    
    # Reward for staying close to center
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    else:
        reward += 0.1
    
    # Reward higher speed (max ~4 m/s)
    if speed > 2.0:
        reward += 0.5 * speed
    
    return float(reward)