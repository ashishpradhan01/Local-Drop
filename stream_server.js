const http=require('http');
const fs=require("fs");
const path=require("path");

const server=http.createServer((req,res)=>{
    if(req.method==='GET'){
        try {
            console.log(req.url)
            const filepath = path.resolve('./media/'+req.url);
            const stat = fs.statSync(filepath)
            const fileSize = stat.size
            const range = req.headers.range
            if (range) {
                const parts = range.replace(/bytes=/, "").split("-")
                const start = parseInt(parts[0], 10)
                const end = parts[1] ?parseInt(parts[1], 10) :fileSize - 1
                const chunksize = (end - start) + 1
                const file = fs.createReadStream(filepath, {start,end})
                const head = {
                    'Content-Range': `bytes ${start}-${end}/${fileSize}`,
                    'Accept-Ranges': 'bytes',
                    'Content-Length': chunksize,
                    // 'Content-Type': 'video/*',
                }
                res.writeHead(206, head);
            file.pipe(res);
            }else{
            const head = {
                'Content-Length': fileSize,
                // 'Content-Type': 'video/*',
            }
            res.writeHead(200, head);
            fs.createReadStream(path).pipe(res);
            }
        }
        catch(err) {
           console.log(`Error: ${err.message}`)
        }
    }
    else{
        res.writeHead(400);
        res.end("bad request");
    }
})


const LOCAL_HOST = '192.168.29.33'
const PORT = process.env.PORT || 3000;

server.listen(PORT, LOCAL_HOST, () => {
  console.log(`server listening on IP: ${LOCAL_HOST} PORT:${PORT}`);
})