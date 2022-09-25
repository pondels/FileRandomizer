mkdir SDtemp
copy *@2x*.png SDtemp
mogrify -format png -resize 50%% SDtemp/*@2x*.png
pushd SDtemp

setlocal enableDelayedExpansion
for %%a in (*.png) do (
    set "filename=%%~nxa"
    set "purged_filename=!filename:@2x=!"
    ren %%~nxa !purged_filename!
)

endlocal
move *.png ..
popd

rmdir /s /q SDtemp