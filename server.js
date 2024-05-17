const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/test/:num', (require, res) => { 
    res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.get('/test2/:num1&:num2', (req, res) => {
    console.log(req.params.num1)
    console.log(req.params.num2)
    res.send('Test2 World!')
  })

app.get('/add/:num1&:num2', (req,res) =>{
  let {num1, num2} = req.params
  let result =  parseInt(num1)+parseInt(num2)
  res.send(num1+num2)
})
var a = [1,2,3,4,5,6,7]

app.get('/search', (req, res) => {
  console.log(req.query)
  console.log(req.query.word)
  console.log(req.query.page)
  if(req.query.word = 1){
    a.forEach(element => {
      console.log(element)
    });
  }
  res.send('search response')
})