class Settings:
	""" To Get Create Settings From JSON File """

	def __init__(self, settings_dict):
		for setting, default_value in settings_dict.items():
			if isinstance(default_value, list):
				default_value = tuple(default_value)

			setattr(self, setting.upper(), default_value)
