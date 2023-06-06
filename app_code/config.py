from configparser import ConfigParser

class AppConfig(object):
    the_config_parser = None

    def __init__(self,config_file_path):
        self.the_config_parser = ConfigParser()
        self.read_config(config_file_path)

    #A function that receives config_file_path. The function prints details about the config files.
    def read_config(self, config_file_path):
        print(self.the_config_parser.read(config_file_path))

        print("config sections are: ", self.the_config_parser.sections())
        print("username:", self.the_config_parser.get('debug', 'user_name'))
        print("port: ", self.the_config_parser.getint('server', 'port'))

    # A function that receives category, name. The function returns the value from the config file in accordance to the parameters. (Strings only)
    def get_string_value(self, category, name):
        return self.the_config_parser.get(category, name)

    # A function that receives category, name. The function returns the value from the config file in accordance to the parameters. (ints only)
    def get_int_value(self, category, name):
        return self.the_config_parser.getint(category, name)

    # A function that receives category, name. The function returns the value from the config file in accordance to the parameters. (booleans only)
    def get_bool_value(self, category, name):
        return self.the_config_parser.getboolean(category, name)

    # A function that returns if the current run is debug values in accordance to the config file.
    def is_using_debug_values(self):
        return self.the_config_parser.getboolean('debug', 'use_debug_values')

    # A function that returns the username value from the config file.
    def get_user_name(self):
        return self.the_config_parser.get('debug', 'user_name')

    # A function that returns the password value from the config file.
    def get_password(self):
        return self.the_config_parser.get('debug', 'user_password')