#!/usr/bin/env python3

"""
Example of drawing a Camera using different norms
"""

from matplotlib.style import use
import matplotlib.pylab as plt
from ctapipe.io import CameraGeometry
from ctapipe.visualization import CameraDisplay
from ctapipe.reco import mock
from matplotlib.colors import PowerNorm

if __name__ == '__main__':

    use('ggplot')
    # load the camera
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    geom = CameraGeometry.from_name("hess", 1)

    titles = 'Linear Scale', 'Log-Scale', 'PowerNorm(gamma=2)'

    model = mock.generate_2d_shower_model(
        centroid=(0.2, 0.0),
        width=0.01,
        length=0.1,
        psi='35d',
    )

    image, sig, bg = mock.make_mock_shower_image(
        geom,
        model.pdf,
        intensity=50,
        nsb_level_pe=1000,
    )

    disps = []
    for ax, title in zip(axs, titles):
        disps.append(CameraDisplay(geom, ax=ax, image=image, title=title))

    disps[0].norm = 'lin'
    disps[1].norm = 'log'
    disps[2].norm = PowerNorm(2)

    for disp in disps:
        disp.add_colorbar(ax=disp.axes)

    plt.tight_layout()
    plt.show()
