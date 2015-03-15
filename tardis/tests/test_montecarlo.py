import numpy as np
from tardis import montecarlo
import pytest

test_line_list = np.array([10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1]).astype(np.float64)

from tardis.montecarlo.wrappers import wrapper

@pytest.fixture
def packet():
    rpacket = {'energy': -1.0,
               'mu': -1,
               'nu': -1.0,
               'nu_line': -1.0,
               'r': -1.0,
               'tau_event': -1.0}
    ret_rpacket = wrapper.struct_to_dict(rpacket)
    return ret_rpacket

def test_rpacket_set_nu(packet):
    assert packet['nu'] == -1.0

def test_rpacket_set_mu(packet):
    assert packet['mu'] == -1

def test_rpacket_set_energy(packet):
    assert packet['energy'] == -1.0

def test_rpacket_set_r(packet):
    assert packet['r'] == -1.0

def test_rpacket_set_tau_event(packet):
    assert packet['tau_event'] == -1.0

def test_rpacket_set_nu_line(packet):
    assert packet['nu_line'] == -1.0

def test_C_value():
    C = wrapper.C_value()
    np.testing.assert_almost_equal(C, 29979245800.0)

def test_get_nu(packet):
    nu = wrapper.get_nu(packet['nu'])
    assert packet['nu'] == nu

def test_get_mu(packet):
    mu = wrapper.get_mu(packet['mu'])
    assert packet['mu'] == mu

def test_get_energy(packet):
    energy = wrapper.get_energy(packet['energy'])
    assert packet['energy'] == energy

def test_get_r(packet):
    r = wrapper.get_r(packet['r'])
    assert packet['r'] == r

def test_get_tau_event(packet):
    tau_event = wrapper.get_tau_event(packet['tau_event'])
    assert packet['tau_event'] == tau_event

def test_get_nu_line(packet):
    nu_line = wrapper.get_nu_line(packet['nu_line'])
    assert packet['nu_line'] == nu_line

# @pytest.mark.parametrize(("insert_value", "expected_insert_position"), [
#     (9.5, 0),
#     (8.5, 1),
#     (7.5, 2),
#     (6.5, 3),
#     (5.5, 4),
#     (5.2, 4),
#     (4.5, 6),
#     (3.5, 7),
#     (2.5, 8),
#     (1.5, 9)])
# def test_binary_search(insert_value, expected_insert_position):
#     insert_position = montecarlo.binary_search_wrapper(test_line_list, insert_value, 0, len(test_line_list))
#     assert insert_position == expected_insert_position


# @pytest.mark.parametrize(("insert_value"), [
#     (10.5),
#     (0.5)])
# def test_binary_search_out_of_bounds(insert_value, capsys):
#     with pytest.raises(ValueError):
#         insert_position = montecarlo.binary_search_wrapper(test_line_list, insert_value, 0, len(test_line_list)-1)

# @pytest.mark.parametrize(("insert_value", "expected_insert_position"), [
#     (10.5, 0),
#     (0.5, len(test_line_list))])
# def test_line_search_out_of_bounds(insert_value, expected_insert_position):
#     insert_position = montecarlo.line_search_wrapper(test_line_list,
#                             insert_value, len(test_line_list))
#     assert insert_position == expected_insert_position

# def test_compute_distance2outer():
#     assert montecarlo.compute_distance2outer_wrapper(0.0, 0.5, 1.0) == 1.0
#     assert montecarlo.compute_distance2outer_wrapper(1.0, 0.5, 1.0) == 0.0
#     assert montecarlo.compute_distance2outer_wrapper(0.3, 1.0, 1.0) == 0.7
#     assert montecarlo.compute_distance2outer_wrapper(0.3, -1.0, 1.0) == 1.3
#     assert montecarlo.compute_distance2outer_wrapper(0.5, 0.0, 1.0) == np.sqrt(0.75)

# def test_compute_distance2inner():
#     assert montecarlo.compute_distance2inner_wrapper(1.5, -1.0, 1.0) == 0.5
#     assert montecarlo.compute_distance2inner_wrapper(0.0, 0.0, 0.0) == montecarlo.miss_distance
#     assert montecarlo.compute_distance2inner_wrapper(1.2, -0.7, 1.0) == 0.3246360509309949

# def test_compute_distance2line():
#     assert montecarlo.compute_distance2line_wrapper(2.20866912e+15, -0.251699059004, 1.05581082105e+15, 1.06020910733e+15, 1693440.0, 5.90513983371e-07, 1.0602263591e+15, 1.06011723237e+15, 2) == 344430881691490.5
#     assert montecarlo.compute_distance2line_wrapper(2.23434667994e+15, -0.291130548401, 1.05581082105e+15, 1.06733618121e+15, 1693440.0, 5.90513983371e-07, 1.06738407486e+15, 1.06732933961e+15, 3) == 96296282395637.2
#     with pytest.raises(RuntimeError):
#         montecarlo.compute_distance2line_wrapper(1.0, 1.0, 1.0, 10.0, 15.0, 1.0 / 15.0, 0.0, 0.0, 0)

# def test_compute_distance2electron():
#     assert montecarlo.compute_distance2electron_wrapper(0.0, 0.0, 2.0, 2.0) == 4.0

