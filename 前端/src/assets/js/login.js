const bubleCreate = () => {
    // 获取body元素
    const body = document.body
    // 创建泡泡元素
    const buble = document.createElement('h4')
    // 设置泡泡半径
    let r = Math.random() * 5 + 25 //半径大小为25~30
    // 设置泡泡的宽高
    buble.style.width = r + 'px'
    buble.style.height = r + 'px'
    // 设置泡泡的随机起点
    buble.style.left = Math.random() * innerWidth + 'px'
    // 为body添加buble元素
    body.append(buble)
    // 4s清除一次泡泡
    setTimeout(() => {
        buble.remove()
    }, 4000)
}
// 每200ms生成一个泡泡
setInterval(() => {
    bubleCreate()
}, 200);