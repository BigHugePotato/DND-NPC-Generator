# NPC Generator Project

## Project Overview

This project focuses on creating a Python-based NPC (Non-Player Character) generator for use in role-playing games. The generator creates diverse characters with attributes, skills, equipment, backstories, and more.

## Files and Components

### Python Scripts

- `npc_generator.py`: The main script that generates random NPCs based on various attributes, skills, and equipment. It imports data from JSON files and includes functions for generating NPCs and their characteristics.

- `app.py`: A Flask-based web application that provides a user-friendly interface for generating NPCs. It imports the `generate_npc` function from `npc_generator.py` and sets up routes for the web interface.

### HTML Templates

- `home.html` and `npc.html`: HTML templates for the web interface. They define the structure of the user interface, including headers, navigation menus, hero sections, galleries, and footers.

### CSS Styles

- `style.css`: A CSS file that contains styling rules for the HTML templates. It defines the visual appearance of various elements such as headers, navigation menus, hero sections, galleries, and footers.

### JSON Data Files

- `alignments.json`: Contains alignment data for NPCs.

- `armor.json`: Defines armor items for NPCs.

- `clothing.json`: Contains clothing items for NPCs.

- `first_names.json` and `last_names.json`: Lists of first and last names for generating NPC names.

- `generic_backstories.json`: Provides generic backstories for NPCs.

- `misc_items.json`: Defines miscellaneous items for NPCs.

- `physical_attributes.json`: Contains physical attributes like height, weight, hair color, etc. for different races.

- `profession_backstories.json`: Contains backstories specific to NPC professions.

- `profession_skills.json`: Defines skills associated with different NPC professions.

- `professions.json`: Lists various NPC professions.

- `races.json`: Contains data about different races for NPCs.

- `skills.json`: Defines skills that NPCs can have.

- `tools.json`: Contains tools used by NPCs.

- `weapons.json`: Defines weapons used by NPCs.
