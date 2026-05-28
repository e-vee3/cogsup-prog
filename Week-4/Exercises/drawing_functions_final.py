from expyriment import design, control, stimuli
import random

def load(stims):
    for s in stims:
        s.preload()

def present_for(stims, t=1000):
    for s in stims:
        s.present()
    exp.clock.wait(t)


## test the functions
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)
control.start()

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

for square in squares:
    stims = [fixation, square]

    t0 = exp.clock.time
    present_for(stims, 500)
    t1 = exp.clock.time

    durations.append(t1 - t0)

print(durations)

control.end()