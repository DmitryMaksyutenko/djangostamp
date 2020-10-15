import os
import filecmp


def insert_between(dest, text, position):
    return (dest[:position + 1] + text + dest[position + 1:])


def dir_cmp(dir1, dir2):
    '''Compares two directories. Returns True in case there are equal.'''
    dirs_cmp = filecmp.dircmp(dir1, dir2)
    #   if any([dirs_cmp.left_only,
    #           dirs_cmp.right_only,
    #           dirs_cmp.funny_files]):
    #       return False
    if len(dirs_cmp.left_only) > 0 or \
       len(dirs_cmp.right_only) > 0 or \
       len(dirs_cmp.funny_files) > 0:
            return False
    (_, mismatch, errors) = filecmp.cmpfiles(dir1, dir2, dirs_cmp.common_files,
                                             shallow=False)
    if len(mismatch) > 0 or len(errors) > 0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not dir_cmp(new_dir1, new_dir2):
            return False
    return True
