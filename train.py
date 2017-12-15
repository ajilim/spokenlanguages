import argparse
import torch
from cfg import CFG

import csv

config = CFG()
train = config.fit
save = config.save

epochs = sum([v for (k, v) in config.epochs])
#train_losses = []
#valid_losses = []
for epoch in range(epochs):
    print("epoch {}".format(epoch + 1))
    train(epoch)
    if config.save_model and (epoch % config.chkpt_interval == 0 or epoch+1 == epochs):
        save(epoch)

is_noisy = "_noisy" if config.mixin_noise else ""
tlosses_name = "output/train_losses_{}{}.csv".format(config.model_name, is_noisy)
with open(tlosses_name, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(config.train_losses)
vlosses = "output/valid_losses_{}{}.csv".format(config.model_name, is_noisy)
with open(vlosses, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(config.valid_losses)
