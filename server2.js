const express = require('express')
const app = express()
const port = 3000
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
const db = require('./config/db.js')

app.get('/person', (req, res)=>{

    db.query('select *from person;', (err, data) => {
        if (!err) {
          console.log(data);
          res.send(data);
        } else {
          res.send(err);
        }
    });
})


app.get('/person/:name',(req,res)=>{
    console.log('/person/:name')
    console.log(req.params.name)
    const name = req.params.name
    db.query(`select *from person where name = '${name}'`,(err,data)=>{
        if(!err){
            console.log(data)
            res.send(data)
        }else{
            res.send(err)
        }
    })
})


app.post('/person', (req,res)=>{
    console.log('/person(post)')
    const { name, age, height } = req.body;
    const query = `INSERT INTO person (name, age, height) VALUES ('${name}', ${age}, ${height})`;
    db.query(query, (err, data) => {
        if (!err) {
            console.log(data);
            res.send(data);
        } else {
            console.error(err);
            res.send(err);
        }
    });

})

app.put('/person', (req,res)=>{
    console.log('/person(put)')
    const {name, age } = req.body
    const query = `update person set age ='${age}' where name = '${name}'`
    db.query(query, (err, data) => {
        if (!err) {
            console.log(data);
            res.send(data);
        } else {
            console.error(err);
            res.send(err);
        }
    });
})

app.delete('/person', (req, res)=>{
    console.log('/person(delete)')
    const {name} = req.body
    const query = `delete from person where name = '${name}'`
    db.query(query, (err, data) => {
        if (!err) {
            console.log(data);
            res.send(data);
        } else {
            console.error(err);
            res.send(err);
        }
    });
})

app.listen(port, ()=>{
    console.log('ex')
} ) 