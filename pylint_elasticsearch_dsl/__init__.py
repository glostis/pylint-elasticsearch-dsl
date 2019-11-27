import astroid

from pylint_elasticsearch_dsl.__about__ import __version__  # noqa


def register(linter):  # pylint: disable=unused-argument
    pass


def q_transform():
    """
    This transform is meant to help astroid infer the type of the object returned by the
    function Q.

    Q is defined here:
    https://github.com/elastic/elasticsearch-dsl-py/blob/master/elasticsearch_dsl/query.py

    Since it has multiple return statements, astroid takes all of them into account, and infers
    that the returned variable can be of the same type as `name_or_query` due to the
    `return name_or_query` branch of the code.

    This transform removes the `return name_or_query` branch of the code from the
    definition of Q, so that astroid understands that the object returned by the function
    is of type Query.

    See https://github.com/PyCQA/pylint/issues/3258 for more info.
    """
    return astroid.parse(
        """
    def Q(name_or_query='match_all', **params):
        # {"match": {"title": "python"}}
        if isinstance(name_or_query, collections_abc.Mapping):
            if params:
                raise ValueError('Q() cannot accept parameters when passing in a dict.')
            if len(name_or_query) != 1:
                raise ValueError('Q() can only accept dict with a single query ({"match": {...}}). '
                     'Instead it got (%r)' % name_or_query)
            name, params = name_or_query.copy().popitem()
            return Query.get_dsl_class(name)(_expand__to_dot=False, **params)

        # MatchAll()
        # if isinstance(name_or_query, Query):
        #     if params:
        #         raise ValueError('Q() cannot accept parameters when passing in a Query object.')
        #     return name_or_query

        # s.query = Q('filtered', query=s.query)
        if hasattr(name_or_query, '_proxied'):
            return name_or_query._proxied

        # "match", title="python"
        return Query.get_dsl_class(name_or_query)(**params)
    """
    )


astroid.register_module_extender(astroid.MANAGER, "elasticsearch_dsl.query", q_transform)
