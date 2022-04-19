"""
This script opens a GUI to check the resulting inverse-gamma distribution. with
the slide-bars one can directly adapt the distribution and check how the shape
of the distribution changes.
"""

from scipy.stats import invgamma
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


if __name__=='__main__':

    window = tk.Tk()
    window.title("Inverse-gamma distribution preview")
    frm_scale = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_scale.pack()
    frm_plot = tk.Frame()
    frm_plot.pack()
    fig = plt.Figure(figsize = (10,10), dpi = 100)
    canvas = FigureCanvasTkAgg(fig,master=frm_plot)
    canvas.draw
    canvas.get_tk_widget().pack()
    ax = fig.add_subplot(111)
    ax.set_xlabel('standard deviation')
    ax.set_ylabel('probability density')
    ax.set_title('inverse-gamma distribution')
    def inv_gamma_plot(varer):
        x_range = np.arange(0.000,0.2,0.00001)
        alpha = var_alpha.get()
        beta = var_beta.get()
        ax.clear()
        ax.set_xlabel('standard deviation')
        ax.set_ylabel('probability density')
        ax.set_title('inverse-gamma distribution')
        ax.plot(np.sqrt(x_range),invgamma.pdf(x_range, alpha, loc = 0,scale = beta ))
        canvas.draw()

    var_alpha = tk.DoubleVar()
    scl_alpha = tk.Scale(frm_scale, label='alpha value', from_=0.001, to=1.00, orient=tk.HORIZONTAL, length=400, showvalue=1,tickinterval=0.999, resolution=0.001, variable = var_alpha, command = inv_gamma_plot)
    scl_alpha.grid(row = 0, column = 2)
    var_beta = tk.DoubleVar()
    scl_beta = tk.Scale(master = frm_scale, label = 'beta value', from_= 0.000001, to = 0.00100,variable = var_beta, orient = tk.HORIZONTAL, length = 400, tickinterval=0.000999, showvalue = 1, resolution = 0.000001,command = inv_gamma_plot)
    scl_beta.grid(row = 1, column = 2)

window.mainloop()
