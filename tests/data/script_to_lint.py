"""This module contains sample code to test how pylint reacts to it
"""
from elasticsearch_dsl import Q


def unary_operator_on_q():
    """This function applies the ~ operator to a Q object

    This normally raises a pylint error
    """
    return ~Q("exists", field="foo")
