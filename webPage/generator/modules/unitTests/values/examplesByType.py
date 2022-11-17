examples = {}

examples[type(None)] = [None]
examples[bool] = [True, False]
examples[int] = [-421, -5, -1, 0, 1, 3, 194]
examples[str] = ["", "Q", "    ", "\r", "\r\n", "oneWord", "two words", "\t\t  {[(1,0\\2,0) + 10] + 2}\r\n<= 12.5;\t  "]
examples[list] = [[], [None], [1, 2, 3], [False, -1], [0, "", [], True], [[1, 2, [3, 4]]]]
examples[dict] = [{}, {"key": "value"}, {1: "one", 2: "two"}, {0: None, 1: [], 2: False, "two": 2}]
examples[tuple] = [(1,), (False, -1), ("string", (2,), None), ([], {}, (), ""), ((1, (2,)),)]
