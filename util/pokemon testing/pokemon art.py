# https://github.com/vsoch/pokemon
import pokemon
from pokemon.skills import get_avatar

# Just get the string!
avatar = get_avatar("pichu", print_screen=True, include_name=False)
