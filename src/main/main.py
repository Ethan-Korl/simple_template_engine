# Make a Templite object.
class Templite:
    def __init__(self, text, *contexts):
        """Construct a Templite with the given `text`.

        `contexts` are dictionaries of values to use for future renderings.
        These are good for filters and global values.

        """
        self.context = {}
        for context in contexts:
            self.context.update(context)
