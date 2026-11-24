# https://gitlab.com/gnfzdz/dotbot-include/-/blob/88e6471cd622625c1ff80478e468f88498c5219d/include.py

import os
import dotbot
from dotbot.cli import read_config
from dotbot.dispatcher import Dispatcher


class Include(dotbot.Plugin):

    '''
    Include the targeted configuration file
    '''

    _directive = 'include'

    def can_handle(self, directive):
        return directive == self._directive
    def handle(self, directive, data):
        if not self.can_handle(directive):
            raise ValueError('%s cannot handle directive %s' % (type(self).__name__, directive))

        filename = data if isinstance(data, str) else data.get('path')
        filename = os.path.expanduser(filename)
        if not os.path.isabs(filename):
            filename = os.path.join(self._context.base_directory(), filename)
        filename = os.path.normpath(filename)
        tasks = read_config([filename])

        defaults = self._context.defaults().get(self._directive, {})
        isolated_default = defaults.get('isolated', False)
        isolated = data.get('isolated', isolated_default) if isinstance(data, dict) else isolated_default

        base_directory = os.path.dirname(filename)
        dispatcher = self._create_dispatcher(base_directory, isolated)
        return self._execute_nested(dispatcher, tasks)

    def _create_dispatcher(self, base_directory, isolated):
        opts = self._context.options()
        kwargs = dict(only=opts.only, skip=opts.skip, options=opts)
        try:
            dispatcher = Dispatcher(base_directory,
                                    plugins=dotbot.Plugin.__subclasses__(), **kwargs)
        except TypeError:
            dispatcher = Dispatcher(base_directory, **kwargs)
        if not isolated:
            # inherit parent defaults, but keep our own base directory
            dispatcher._context.set_defaults(self._context.defaults())
        return dispatcher

    def _execute_nested(self, dispatcher, data):
        # if the data is a dictionary, wrap it in a list
        data = data if type(data) is list else [ data ]
        return dispatcher.dispatch(data)
