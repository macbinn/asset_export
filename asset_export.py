import os
import inkex
from inkex.command import inkscape


EXPORT_DPIS = [
    96,
    192,
    288,
]


class AssetExportExtension(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--export_file_name", default=os.path.expanduser("~/Desktop/asset.png"))

    def effect(self):
        if len(self.options.ids) == 0:
            self.msg("No object selected")
            return
        
        node_id = self.options.ids[0]
        path = self.options.export_file_name
        for i, dpi in enumerate(EXPORT_DPIS):
            if i > 0:
                outpath = f"{path[:-4]}@{i + 1}x.png"
            else:
                outpath = path
            self.export_dpi(node_id, dpi, outpath)

    def export_dpi(self, node_id, dpi, path):
        kwargs = {
            'export-id': node_id,
            'export-filename': path,
            'export-dpi': str(dpi),
        }
        svg_file = self.options.input_file 
        inkscape(svg_file, **kwargs)


if __name__ == "__main__":
    AssetExportExtension().run()
