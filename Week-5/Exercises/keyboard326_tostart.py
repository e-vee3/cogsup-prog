from expyriment import design, control, stimuli

""" Global settings """
exp = design.Experiment(name = "press a key")
control.set_develop_mode()
control.initialize(exp)

# present cue
cue = stimuli.TextLine("PRESS A KEY")
cue.present()

# waits for a keypress - THIS IS WRONG THERE IS NO WAIT FOR KEYPRESS NEED TO CHANGE TO CORRECT VARIABLE
key, _ = control.wait_for_keypress()

# shows feedback
feedback = stimuli.TextLine("YOU PRESSED " + str(key))
feedback.present()

exp.clock.wait(3000)

control.end()

