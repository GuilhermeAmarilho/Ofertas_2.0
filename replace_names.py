import os
from pathlib import Path

# Mapeamento de nomes antigos para novos
MAPPING = {
    'vertical': 'Retrato',
    'horizontal': 'Paisagem',
    'feed': 'Quadrado',
    'story': 'Longo'
}

# Diretório base onde ficam os temas
BASE_DIR = Path(__file__).parent / 'Design' / 'Themes'


def rename_images_in_themes(base_dir: Path):
    if not base_dir.exists() or not base_dir.is_dir():
        print(f"Diretório não encontrado: {base_dir}")
        return

    for theme_dir in base_dir.iterdir():
        if not theme_dir.is_dir():
            continue
        print(f"Processando tema: {theme_dir.name}")

        for img_path in theme_dir.iterdir():
            if not img_path.is_file():
                continue

            stem = img_path.stem.lower()
            if stem in MAPPING:
                new_name = MAPPING[stem] + img_path.suffix
                new_path = theme_dir / new_name
                try:
                    img_path.rename(new_path)
                    print(f"Renomeado: {img_path.name} -> {new_name}")
                except Exception as e:
                    print(f"Erro ao renomear {img_path.name}: {e}")

rename_images_in_themes(BASE_DIR)
