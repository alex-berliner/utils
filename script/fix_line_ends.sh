function fix_lines()
{
    for var in "$@"
    do
        dos2unix -n $var $var
    done
}

export -f fix_lines
# https://unix.stackexchange.com/a/158569
find "$1" | grep -E ".*(sh$)|(py$)" | xargs bash -c 'fix_lines "$@"'
