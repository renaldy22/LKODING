const express = require("express")
const mysql = require("mysql")
const BodyParser = require("body-parser")
const app = express()

app.set("view engine", "ejs")
app.set("views", "views")
app.use(BodyParser.urlencoded({ extended: true}))
const db = mysql.createConnection({
    host : "localhost",
    database : "mahasiswa",
    user : "root",
    password: "",
})

db.connect((err) => {
    if (err) throw err
    // untuk ambil data
    app.get("/", (req, res) => {
        const sql = "SELECT * FROM table_mahasiswa" 
        db.query(sql,(err, result) => {
            const mahasiswas = JSON.parse(JSON.stringify(result))
            console.log('hasil database ->',mahasiswas)    
            res.render("index", {users : mahasiswas, title : "DAFTAR MURID"})
        })
    })
        // untuk insert data
        app.post("/tambah", (req, res) => {
            const InsertSql = `INSERT INTO table_mahasiswa (nama, kelas) VALUES ('${req.body.nama}', '${req.body.kelas}');`
            db.query(InsertSql, (err, result) => {
                if (err) throw err
                res.redirect("/");
            })
        })
})



app.listen(3000, () => {
    console.log("server ready..")
})