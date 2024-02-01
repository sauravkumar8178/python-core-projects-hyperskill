def manage_collide(bolts, aliens):
    # Check if a bolt collides with any alien(s)
    for b in bolts:
        for a in aliens:
            if b['rect'].colliderect(a['rect']):
                for a in aliens:
                    a['health'] -= 1
                    bolts.remove(b)
                    if a['health'] == 0:
                        aliens.remove(a)
    # Return bolts, aliens dictionaries
    return bolts, aliens
	
	
	
	
	    