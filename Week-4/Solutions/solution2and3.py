def draw(stims):
# Clear first, update last
    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == len(stims) - 1))

def draw(stims):

    # Clear the back buffer
    exp.screen.clear()

    # Draw to back buffer
    for stim in stims:
        stim.present(clear=False, update=False)
        
    # Swap the buffers
    exp.screen.update()