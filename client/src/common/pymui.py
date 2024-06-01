# __pragma__ ('skip')
from common import require
# __pragma__ ('noskip')


# Icons
MenuIcon = require('@mui/icons-material/Menu')['default']
CloseIcon = require('@mui/icons-material/Close')['default']
AddIcon = require('@mui/icons-material/AddCircle')['default']

# Basic components
Button = require('@mui/material/Button')['default']
ButtonGroup = require('@mui/material/ButtonGroup')['default']
IconButton = require('@mui/material/IconButton')['default']
InputLabel = require('@mui/material/InputLabel')['default']
OutlinedInput = require('@mui/material/OutlinedInput')['default']
TextField = require('@mui/material/TextField')['default']
Select = require('@mui/material/Select')['default']
Box = require('@mui/material/Box')['default']
Toolbar = require('@mui/material/Toolbar')['default']
AppBar = require('@mui/material/AppBar')['default']
Typography = require('@mui/material/Typography')['default']
Divider = require('@mui/material/Divider')['default']
Container = require('@mui/material/Container')['default']
Input = require('@mui/material/Input')['default']
Tooltip = require('@mui/material/Tooltip')['default']
Menu = require('@mui/material/Menu')['default']
MenuItem = require('@mui/material/MenuItem')['default']
Paper = require('@mui/material/Paper')['default']
CircularProgress = require('@mui/material/CircularProgress')['default']
Link = require('@mui/material/Link')['default']
Radio = require('@mui/material/Radio')['default']
RadioGroup = require('@mui/material/RadioGroup')['default']
FormControl = require('@mui/material/FormControl')['default']
FormLabel = require('@mui/material/FormLabel')['default']
FormControlLabel = require('@mui/material/FormControlLabel')['default']

# Tables
TableContainer = require('@mui/material/TableContainer')['default']
Table = require('@mui/material/Table')['default']
TableHead = require('@mui/material/TableHead')['default']
TableBody = require('@mui/material/TableBody')['default']
TableFooter = require('@mui/material/TableFooter')['default']
TableRow = require('@mui/material/TableRow')['default']
TableCell = require('@mui/material/TableCell')['default']

# Theming
ThemeProvider = require('@mui/styles/ThemeProvider')['default']
createMuiTheme = require('@mui/material/styles/createTheme')['default']
useTheme = require('@mui/styles/useTheme')['default']
styled = require('@mui/styles/styled')['default']
makeStyles = require('@mui/styles/makeStyles')['default']
colors = require('@mui/material/colors')

# notistack
notistack = require('notistack')

SnackbarProvider = notistack.SnackbarProvider
useSnackbar = notistack.useSnackbar