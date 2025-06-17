const size = 5 ;
for(let i = 0 ;i < size;i++){
    let row = ''
    for(let j = 0;j < i + 1 ;j++ ){
        row += '*'
    }
    console.log(row)
}