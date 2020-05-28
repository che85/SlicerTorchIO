import qt

from .Transform import Transform


class RandomAffine(Transform):
    def setup(self):
        scales = self.getDefaultValue('scales')
        self.scalesSlider = self.makeSlider(0.5, *scales, 2, 0.01, 'scales')
        self.layout.addRow('Scales: ', self.scalesSlider)

        degrees = self.getDefaultValue('degrees')
        self.degreesSlider = self.makeSlider(
            -180, -degrees, degrees, 180, 1, 'degrees')
        self.layout.addRow('Degrees: ', self.degreesSlider)

        self.interpolationComboBox = self.makeInterpolationComboBox()
        self.layout.addRow('Interpolation: ', self.interpolationComboBox)

        self.isotropicCheckBox = qt.QCheckBox('Isotropic')
        self.layout.addWidget(self.isotropicCheckBox)

        arg = 'default_pad_value'
        self.padLineEdit = qt.QLineEdit(self.getDefaultValue(arg))
        self.padLineEdit.setToolTip(self.getArgDocstring(arg))
        self.layout.addRow('Padding: ', self.padLineEdit)

    def getPadArg(self):
        text = self.padLineEdit.text
        try:
            value = float(text)
        except ValueError:
            value = text
        return value

    def getKwargs(self):
        kwargs = dict(
            scales=self.getSliderRange(self.scalesSlider),
            degrees=self.getSliderRange(self.degreesSlider),
            isotropic=self.isotropicCheckBox.isChecked(),
            image_interpolation=self.getInterpolation(),
            default_pad_value=self.getPadArg(),
        )
        return kwargs