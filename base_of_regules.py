


class BaseOfRegules:

    def __init__(self):
        e_du = {"se_du": "DU", "se_su": "DU", "se_mu": "DU", "se_z": "DU", "se_md": "SU", "se_sd": "MU","se_dd": "Z"}
        e_su = {"se_du": "DU", "se_su": "DU", "se_mu": "DU", "se_z": "SU", "se_md": "MU", "se_sd": "Z", "se_dd": "MD"}
        e_mu = {"se_du": "DU", "se_su": "DU", "se_mu": "SU", "se_z": "MU", "se_md": "Z", "se_sd": "MD", "se_dd": "SD"}
        e_z = {"se_du": "DU", "se_su": "SU", "se_mu": "MU", "se_z": "Z", "se_md": "MD", "se_sd": "SD", "se_dd": "DD"}
        e_md = {"se_du": "SU", "se_su": "MU", "se_mu": "Z", "se_z": "MD", "se_md": "SD", "se_sd": "DD", "se_dd": "DD"}
        e_sd = {"se_du": "MU", "se_su": "Z", "se_mu": "MD", "se_z": "SD", "se_md": "DD", "se_sd": "DD", "se_dd": "DD"}
        e_dd = {"se_du": "Z", "se_su": "MD", "se_mu": "SD", "se_z": "DD", "se_md": "DD", "se_sd": "DD", "se_dd": "DD"}
        self. data = {
            "e_du": e_du,
            "e_su": e_su,
            "e_mu": e_mu,
            "e_z": e_z,
            "e_md": e_md,
            "e_sd": e_sd,
            "e_dd": e_dd
        }