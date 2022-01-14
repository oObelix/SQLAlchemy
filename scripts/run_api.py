from root.main_section import MS
from root.main_section import session

if __name__ == '__main__':
    print(MS.select())
    print(MS.select_scalars())
    print(MS.inner_join())
    print(MS.outer_join())
    # print(MS.outer_join_())
