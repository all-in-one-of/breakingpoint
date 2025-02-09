import pymel.core as pm
from alShaders import *

class AEalLayerColorTemplate(alShadersTemplate):
	controls = {}
	params = {}
	def setup(self):
		self.params.clear()
		self.params["layer1"] = Param("layer1", "Layer 1", "The background layer (will be blended over black if its alpha is not 1.", "rgb", presets=None)
		self.params["layer1a"] = Param("layer1a", "Layer 1 Alpha", "The alpha of the background layer", "float", presets=None)
		self.params["layer1blend"] = Param("layer1blend", "Mode", "Blend mode for the background layer.", "enum", presets=None)
		self.params["layer2"] = Param("layer2", "Layer 2", "The color plugged in here will be blended over the layers below according to its alpha and blend mode.", "rgb", presets=None)
		self.params["layer2a"] = Param("layer2a", "Layer 2 Alpha", "The alpha used to blend this layer over the layers below.", "float", presets=None)
		self.params["layer2blend"] = Param("layer2blend", "Mode", "The blend mode used to blend this layer over the layers below.", "enum", presets=None)
		self.params["layer3"] = Param("layer3", "Layer 3", "The color plugged in here will be blended over the layers below according to its alpha and blend mode.", "rgb", presets=None)
		self.params["layer3a"] = Param("layer3a", "Layer 3 Alpha", "The alpha used to blend this layer over the layers below.", "float", presets=None)
		self.params["layer3blend"] = Param("layer3blend", "Mode", "The blend mode used to blend this layer over the layers below.", "enum", presets=None)
		self.params["layer4"] = Param("layer4", "Layer 4", "The color plugged in here will be blended over the layers below according to its alpha and blend mode.", "rgb", presets=None)
		self.params["layer4a"] = Param("layer4a", "Layer 4 Alpha", "The alpha used to blend this layer over the layers below.", "float", presets=None)
		self.params["layer4blend"] = Param("layer4blend", "Mode", "The blend mode used to blend this layer over the layers below.", "enum", presets=None)
		self.params["layer5"] = Param("layer5", "Layer 5", "The color plugged in here will be blended over the layers below according to its alpha and blend mode.", "rgb", presets=None)
		self.params["layer5a"] = Param("layer5a", "Layer 5 Alpha", "The alpha used to blend this layer over the layers below.", "float", presets=None)
		self.params["layer5blend"] = Param("layer5blend", "Mode", "The blend mode used to blend this layer over the layers below.", "enum", presets=None)
		self.params["layer6"] = Param("layer6", "Layer 6", "The color plugged in here will be blended over the layers below according to its alpha and blend mode.", "rgb", presets=None)
		self.params["layer6a"] = Param("layer6a", "Layer 6 Alpha", "The alpha used to blend this layer over the layers below.", "float", presets=None)
		self.params["layer6blend"] = Param("layer6blend", "Mode", "The blend mode used to blend this layer over the layers below.", "enum", presets=None)
		self.params["layer7"] = Param("layer7", "Layer 7", "The color plugged in here will be blended over the layers below according to its alpha and blend mode.", "rgb", presets=None)
		self.params["layer7a"] = Param("layer7a", "Layer 7 Alpha", "The alpha used to blend this layer over the layers below.", "float", presets=None)
		self.params["layer7blend"] = Param("layer7blend", "Mode", "The blend mode used to blend this layer over the layers below.", "enum", presets=None)
		self.params["layer8"] = Param("layer8", "Layer 8", "The color plugged in here will be blended over the layers below according to its alpha and blend mode.", "rgb", presets=None)
		self.params["layer8a"] = Param("layer8a", "Layer 8 Alpha", "The alpha used to blend this layer over the layers below.", "float", presets=None)
		self.params["layer8blend"] = Param("layer8blend", "Mode", "The blend mode used to blend this layer over the layers below.", "enum", presets=None)

		self.addSwatch()
		self.beginScrollLayout()

		self.addCustomRgb("layer1")
		self.addCustomFlt("layer1a")
		self.addControl("layer1blend", label="Mode", annotation="Blend mode for the background layer.")
		self.addCustomRgb("layer2")
		self.addCustomFlt("layer2a")
		self.addControl("layer2blend", label="Mode", annotation="The blend mode used to blend this layer over the layers below.")
		self.addCustomRgb("layer3")
		self.addCustomFlt("layer3a")
		self.addControl("layer3blend", label="Mode", annotation="The blend mode used to blend this layer over the layers below.")
		self.addCustomRgb("layer4")
		self.addCustomFlt("layer4a")
		self.addControl("layer4blend", label="Mode", annotation="The blend mode used to blend this layer over the layers below.")
		self.addCustomRgb("layer5")
		self.addCustomFlt("layer5a")
		self.addControl("layer5blend", label="Mode", annotation="The blend mode used to blend this layer over the layers below.")
		self.addCustomRgb("layer6")
		self.addCustomFlt("layer6a")
		self.addControl("layer6blend", label="Mode", annotation="The blend mode used to blend this layer over the layers below.")
		self.addCustomRgb("layer7")
		self.addCustomFlt("layer7a")
		self.addControl("layer7blend", label="Mode", annotation="The blend mode used to blend this layer over the layers below.")
		self.addCustomRgb("layer8")
		self.addCustomFlt("layer8a")
		self.addControl("layer8blend", label="Mode", annotation="The blend mode used to blend this layer over the layers below.")

		pm.mel.AEdependNodeTemplate(self.nodeName)
		self.addExtraControls()

		self.endScrollLayout()
