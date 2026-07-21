"""Auto-generated migration.

Created: 2026-06-19 23:37:30
"""

depends_on = None


def upgrade(ctx):
    """Apply migration."""
    ctx.create_table(
        "user",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'email',
                'python_type': 'emailstr',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': True,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'password',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'fullname',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'active',
                'python_type': 'bool',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': 'false',
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'admin',
                'python_type': 'bool',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': 'false',
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'omemo_bundle',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
    )
    ctx.create_table(
        "project",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'name',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': True,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'description',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'updated_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_by_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_project_created_by_id',
                'columns': [
                    'created_by_id'
                ],
                'ref_table': 'user',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'SET NULL',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "board",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'name',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'description',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'updated_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'project_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_board_project_id',
                'columns': [
                    'project_id'
                ],
                'ref_table': 'project',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "board_column",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'name',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'position',
                'python_type': 'int',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': '0',
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'updated_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'board_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_board_column_board_id',
                'columns': [
                    'board_id'
                ],
                'ref_table': 'board',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "task",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'title',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'description',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'position',
                'python_type': 'int',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': '0',
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'updated_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'column_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'assignee_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'parent_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_task_column_id',
                'columns': [
                    'column_id'
                ],
                'ref_table': 'board_column',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            },
            {
                'name': 'fk_task_assignee_id',
                'columns': [
                    'assignee_id'
                ],
                'ref_table': 'user',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'SET NULL',
                'on_update': 'CASCADE'
            },
            {
                'name': 'fk_task_parent_id',
                'columns': [
                    'parent_id'
                ],
                'ref_table': 'task',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'SET NULL',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "project_group",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'name',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'description',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'updated_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'project_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_project_group_project_id',
                'columns': [
                    'project_id'
                ],
                'ref_table': 'project',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "project_group_permission",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'permission',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'group_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_project_group_permission_group_id',
                'columns': [
                    'group_id'
                ],
                'ref_table': 'project_group',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "project_member",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'group_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'user_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_project_member_group_id',
                'columns': [
                    'group_id'
                ],
                'ref_table': 'project_group',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            },
            {
                'name': 'fk_project_member_user_id',
                'columns': [
                    'user_id'
                ],
                'ref_table': 'user',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "theme",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'name',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': True,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'bg_color',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'bg_secondary_color',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'color_primary',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'color_lightGrey',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'color_grey',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'color_darkGrey',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'color_error',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'color_success',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'grid_maxWidth',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'grid_gutter',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'font_size',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'font_color',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'font_family_sans',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'font_family_mono',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
    )
    ctx.create_table(
        "role",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'name',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': True,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
    )
    ctx.create_table(
        "user_role",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'user_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'role_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_user_role_user_id',
                'columns': [
                    'user_id'
                ],
                'ref_table': 'user',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            },
            {
                'name': 'fk_user_role_role_id',
                'columns': [
                    'role_id'
                ],
                'ref_table': 'role',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "mailing_list",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'name',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': True,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'address',
                'python_type': 'emailstr',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': True,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'distribution_address',
                'python_type': 'emailstr',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': True,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'archive_address',
                'python_type': 'emailstr',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': True,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'description',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'public',
                'python_type': 'bool',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': 'true',
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'archive_enabled',
                'python_type': 'bool',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': 'true',
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'moderation_enabled',
                'python_type': 'bool',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': 'false',
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'principal_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'inbox_principal_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'archive_principal_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'updated_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
    )
    ctx.create_table(
        "moderation_message",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'message_id',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'subject',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'sender',
                'python_type': 'emailstr',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'sent_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'text_body',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'html_body',
                'python_type': 'str',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'status',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': "'pending'",
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'decided_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'mailing_list_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_moderation_message_mailing_list_id',
                'columns': [
                    'mailing_list_id'
                ],
                'ref_table': 'mailing_list',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            }
        ],
    )
    ctx.create_table(
        "pending_subscriber",
        fields=[
            {
                'name': 'id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': True,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'email',
                'python_type': 'emailstr',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'token',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'action',
                'python_type': 'str',
                'db_type': None,
                'nullable': False,
                'primary_key': False,
                'unique': False,
                'default': "'subscribe'",
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'created_at',
                'python_type': 'datetime',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            },
            {
                'name': 'mailing_list_id',
                'python_type': 'int',
                'db_type': None,
                'nullable': True,
                'primary_key': False,
                'unique': False,
                'default': None,
                'auto_increment': False,
                'max_length': None,
                'max_digits': None,
                'decimal_places': None
            }
        ],
        foreign_keys=[
            {
                'name': 'fk_pending_subscriber_mailing_list_id',
                'columns': [
                    'mailing_list_id'
                ],
                'ref_table': 'mailing_list',
                'ref_columns': [
                    'id'
                ],
                'on_delete': 'CASCADE',
                'on_update': 'CASCADE'
            }
        ],
    )


def downgrade(ctx):
    """Revert migration."""
    ctx.drop_table("pending_subscriber")
    ctx.drop_table("moderation_message")
    ctx.drop_table("mailing_list")
    ctx.drop_table("user_role")
    ctx.drop_table("role")
    ctx.drop_table("theme")
    ctx.drop_table("project_member")
    ctx.drop_table("project_group_permission")
    ctx.drop_table("project_group")
    ctx.drop_table("task")
    ctx.drop_table("board_column")
    ctx.drop_table("board")
    ctx.drop_table("project")
    ctx.drop_table("user")
