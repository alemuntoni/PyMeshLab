import pymeshlab as ml
from . import samples_common


def test_save_filter_script():
    print('\n')
    base_path = samples_common.samples_absolute_path()
    output_path = samples_common.test_output_path()

    # create a new MeshSet
    ms = ml.MeshSet()

    # load a new mesh
    ms.load_new_mesh(base_path + "cube.obj")

    # applying some filter to the mesh...
    # every apply_filter saves in the filter script stored in the MeshSet
    # the applied filter with their parameters
    ms.apply_filter('remeshing_isotropic_explicit_remeshing')
    ms.apply_filter('remeshing_isotropic_explicit_remeshing')
    ms.apply_filter('per_face_quality_according_to_triangle_shape_and_aspect_ratio')
    ms.apply_filter('colorize_by_face_quality')

    # save the mesh
    ms.save_current_mesh(output_path + 'col_rem_cube.ply')

    # save the current filter script, containing all the filters with their parameters
    # that have been applied in the MeshSet ms.
    ms.save_filter_script(output_path + 'test_saved_script.mlx')
