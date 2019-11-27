from elasticsearch_dsl import Q


def main():
    return ~Q("exists", field="foo")
