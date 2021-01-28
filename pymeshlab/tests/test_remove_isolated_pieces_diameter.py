import pymeshlab as ml
from . import samples_common


def test_remove_isolated_pieces_diameter():
    print('\n')
    base_path = samples_common.samples_absolute_path()
    output_path = samples_common.test_output_path()

    # create a new MeshSet
    ms = ml.MeshSet()

    ms.load_new_mesh(base_path + "rangemaps/face000.ply")

    assert ms.number_meshes() == 1

    assert ms.current_mesh().face_number() == 166259

    # create a new object of type Percentage, with value 50%
    p = ml.Percentage(50)

    # apply the filter that will remove connected components having diameter less than 50%
    # of the diameter of the entire mesh
    ms.apply_filter('remove_isolated_pieces_wrt_diameter', mincomponentdiag=p)

    assert ms.current_mesh().face_number() == 161606

    ms.save_current_mesh(output_path + 'face000_clean_by_diameter.ply')
