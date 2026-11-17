# Ignoring some linting rules in tests
# pylint: disable=missing-docstring
# pylint: disable=unused-variable

import pytest

def test_cpp_agraph():
    try:
        from bingocpp import AGraph
        bingocpp = True
    except ModuleNotFoundError:
        bingocpp = False

    if not bingocpp:
        pytest.skip("Bingocpp AGraph could not be loaded."
                                  " Its tests will be skipped.")


def test_cpp_evaluation_backend():
    try:
        from bingocpp import evaluation_backend
        bingocpp = True
    except ModuleNotFoundError:
        bingocpp = False

    if not bingocpp:
        pytest.skip("Bingocpp evaluation_backend could not be "
                                  "loaded."
                                  " Its tests will be skipped.")


def test_cpp_simplification_backend():
    try:
        from bingocpp import simplification_backend
        bingocpp = True
    except ModuleNotFoundError:
        bingocpp = False

    if not bingocpp:
        pytest.skip("Bingocpp simplification_backend could not "
                                  "be loaded."
                                  " Its tests will be skipped.")


def test_cpp_implicit_regression():
    try:
        from bingocpp import ImplicitTrainingData, ImplicitRegression, \
                             Equation
        bingocpp = True
    except ModuleNotFoundError:
        bingocpp = False

    if not bingocpp:
        pytest.skip("Bingocpp implicit regression classes could"
                                  " not be loaded."
                                  " Its tests will be skipped.")


def test_cpp_explicit_regression():
    try:
        from bingocpp import ExplicitTrainingData, ExplicitRegression, \
                             Equation
        bingocpp = True
    except ModuleNotFoundError:
        bingocpp = False

    if not bingocpp:
        pytest.skip("Bingocpp explicit regression classes could"
                                  " not be loaded."
                                  " Its tests will be skipped.")


def test_cpp_gradient_mixins():
    try:
        from bingocpp import GradientMixin, \
                             VectorGradientMixin, \
                             VectorBasedFunction
        bingocpp = True
    except ModuleNotFoundError:
        bingocpp = False

    if not bingocpp:
        pytest.skip("Bingocpp gradient mixin classes could"
                                  " not be loaded."
                                  " Its tests will be skipped.")
