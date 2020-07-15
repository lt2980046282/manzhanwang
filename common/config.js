let url_config = ""

if(process.env.NODE_ENV === 'development'){
    // 开发环境
    url_config = 'https://*****.com/'
}else{
    // 生产环境
    url_config = 'https://*****.com/'
}

export default url_config