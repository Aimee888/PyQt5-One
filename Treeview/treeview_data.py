class DataCollection:
    def __init__(self):
        self.module = {}
        self.items = []

    def set_module(self, module_dic):
        self.module = module_dic

    def add_item(self, item_dic):
        self.items.append(item_dic)

    def set_item(self, item_dic, item_name):
        for item_num, item in enumerate(self.items):
            for name, result in item.items():
                if name == item_name:
                    self.items[item_num][name] = item_dic[name]
                    break
        all_pass = True
        for item1 in self.items:
            for result1 in item1.values():
                if result1 != "p":
                    all_pass = False
                    break
        if all_pass:
            for module_name, module_result in self.module.items():
                self.module[module_name] = "p"


if __name__ == "__main__":
    module_1 = DataCollection()
    module_1.set_module({"Test1": "t"})
    module_1.add_item({"a": "t"})
    module_1.add_item({"b": "t"})
    module_1.add_item({"c": "t"})
    module_1.add_item({"d": "t"})
    module_1.set_item({"a": "p"}, "a")
    module_1.set_item({"b": "p"}, "b")
    module_1.set_item({"c": "p"}, "c")
    module_1.set_item({"d": "p"}, "d")
