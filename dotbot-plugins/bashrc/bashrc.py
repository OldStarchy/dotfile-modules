import os
import dotbot


class Bashrc(dotbot.Plugin):
    '''
    Add a `source <file>` line to ~/.bashrc for the targeted file
    '''

    _directive = 'bashrc'

    def can_handle(self, directive):
        return directive == self._directive

    def handle(self, directive, data):
        if not self.can_handle(directive):
            raise ValueError('%s cannot handle directive %s' % (type(self).__name__, directive))

        if not isinstance(data, str):
            self._log.error('bashrc directive expects a single path string, got %r' % (data,))
            return False

        filename = os.path.expanduser(data)
        if not os.path.isabs(filename):
            filename = os.path.join(self._context.base_directory(), filename)
        filename = os.path.normpath(filename)

        if not os.path.exists(filename):
            self._log.warning('%s does not exist (adding source line anyway)' % filename)

        bashrc_path = os.path.expanduser('~/.bashrc')
        source_line = 'source "%s"' % filename

        try:
            # 'a+' creates the file if missing; writes always append regardless of seek position
            with open(bashrc_path, 'a+') as bashrc_file:
                bashrc_file.seek(0)
                contents = bashrc_file.read()
                if source_line not in contents.splitlines():
                    bashrc_file.write('%s\n' % source_line)
                    self._log.lowinfo('Added "%s" to %s' % (source_line, bashrc_path))
                else:
                    self._log.lowinfo('%s already sources %s' % (bashrc_path, filename))
        except OSError as e:
            self._log.error('Failed to update %s: %s' % (bashrc_path, e))
            return False

        return True
