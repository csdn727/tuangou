from util import spaces2nbsp
from xml2json import ensureAscii


class Deal(object):
    ''' single deal instance '''

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def next(self):
        n = self._i.next().name
        return n, getattr(self, n)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def to_dict(self):
        return self.__dict__.copy()

    def _trim(self):
        for key in ['title', 'cate', 'subcate']:
            value = getattr(self, key, "")
            setattr(self, key, spaces2nbsp(ensureAscii(value)))

        for key in ['value', 'price', 'time']:
            value = getattr(self, key, 0)
            try:
                setattr(self, key, int(float(value)))
            except:
                pass

    @classmethod
    def create_item(cls, kwargs):
        item = cls()
        for field in cls.create_required_fields():
            setattr(item, field, kwargs.get(field))
        item._trim()
        return item

    def update_item(self, kwargs):
        change_str = ""
        for field in self.update_fields():
            if field in kwargs:
                old_val = getattr(self, field, None)
                new_val = kwargs.get(field)
                if old_val != new_val:
                    setattr(self, field, new_val)
                    if change_str != '':
                        change_str += ';'
                    change_str += '(%s)%s=>%s' % (field, old_val, new_val)
        if change_str != '':
            print "create ok!", change_str
        return change_str

    @classmethod
    def create_required_fields(cls):
        return ['title', 'price', 'value', 'cate', 'subcate', 'url', 'time']

    @classmethod
    def update_fields(cls):
        return ['title', 'price', 'value', 'cate', 'subcate', 'url', 'time']

    def __repr__(self):

        keys = ['title', 'price', 'value', 'cate', 'subcate', 'url']
        values = [str(getattr(self, key)) for key in keys]
        return " ".join(values)
