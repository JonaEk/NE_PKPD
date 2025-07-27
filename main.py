import numpy as np
import matplotlib.pyplot as plt
import sund

sund.install_model('./models/SUND_PKPD_NE.txt')
print(sund.installed_models())