if __name__ == '__main__':
    bar = {"caffe": 1, "cappuccino": 2, "cornetto": 2, "spremuta": 3}
    print(bar["cornetto"])
    bar["caffe"] = 2
    print(bar["cornetto"])
    prodotti = bar.keys()
    print(prodotti)
    bar.update({"cioccolata": 3, "krapfen": 2})
    print(bar)
    krapfen = bar.pop("krapfen", 0)
    print(krapfen)
    print(bar)