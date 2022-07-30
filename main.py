from uuid import uuid4
import timeit


need_items = 10


print(f"{need_items=}")


def loop1() -> int:
    result = 0
    for num in range(need_items):
        result += num
    return result


def loop2() -> int:
    result = 0
    for num in range(need_items):
        result += 1
    return result


def loop3() -> int:
    result = 0
    for num in range(need_items):
        result += 1
        print(f"loop3 printed {result=}", end='\r')
    print(end="\n")
    return result


def loop4() -> int:

    db = []

    def generate_id():
        _uuid_list = []

        for i in range(1, 5):
            _uuid_list.append(str(uuid4()))

        _id = "-".join(_uuid_list)

        if _id not in db:
            return _id
        return generate_id()

    for num in range(need_items):
        db.append(generate_id())

    return len(db)


def loop5() -> int:

    db = []

    def generate_id():
        _uuid_list = []

        _uuid_list.append(str(uuid4()))
        _uuid_list.append(str(uuid4()))
        _uuid_list.append(str(uuid4()))
        _uuid_list.append(str(uuid4()))

        _id = "-".join(_uuid_list)

        if _id not in db:
            return _id
        return generate_id()

    for num in range(need_items):
        db.append(generate_id())

    return len(db)


def loop6() -> int:

    db = []

    def generate_id():
        _uuid_list = [
            str(uuid4()),
            str(uuid4()),
            str(uuid4()),
            str(uuid4())
        ]

        _id = "-".join(_uuid_list)

        if _id not in db:
            return _id
        return generate_id()

    for num in range(need_items):
        db.append(generate_id())

    return len(db)


def loop7() -> int:
    db = []

    for num in range(need_items):
        _id = "-".join([
            str(uuid4()),
            str(uuid4()),
            str(uuid4()),
            str(uuid4())
        ])

        db.append(_id)

    return len(db)


def loop8() -> int:
    db = []

    for num in range(need_items):
        _id = "-".join([
            str(uuid4()),
            str(uuid4()),
            str(uuid4()),
            str(uuid4())
        ])

        db.append(_id)

    return len(db)


def loop9() -> int:
    db = []

    for num in range(need_items):
        _id = "-".join([
            str(uuid4()),
            str(uuid4()),
            str(uuid4()),
            str(uuid4())
        ])

        if _id not in db:
            db.append(_id)
        else:
            continue
    print(f"nine loop db count: {len(db)}")
    return len(db)


print(f"\nFor speed test:")
print(f"loop1: {round(timeit.timeit(loop1, number=1), 5)}s")
print(f"loop2: {round(timeit.timeit(loop2, number=1), 5)}s")
print(f"loop3: {round(timeit.timeit(loop3, number=1), 5)}s")

print(f"\nGenerate _id speed test:")
print(f"loop4: {round(timeit.timeit(loop4, number=1), 5)}s")
print(f"loop5: {round(timeit.timeit(loop5, number=1), 5)}s")
print(f"loop6: {round(timeit.timeit(loop6, number=1), 5)}s")
print(f"loop7: {round(timeit.timeit(loop7, number=1), 5)}s")
print(f"loop8: {round(timeit.timeit(loop8, number=1), 5)}s")

print(f"\nProduction solution:")
loop9_time = timeit.timeit(loop9, number=1)
print(f"loop9: {round(loop9_time, 5)}s")
print(
    f"loop9 {need_items}*2={need_items*2} about time: {round(loop9_time*2.2, 5)}s")
print(
    f"loop9 {need_items}*10={need_items*10} about time: {round(loop9_time*15, 5)}s")
print(
    f"loop9 {need_items}*100={need_items*100} about time: {round(loop9_time*150, 5)}s")
print(f"loop9 {need_items}*1000={need_items*1000} about time: {round(loop9_time*4500, 5)}s")

