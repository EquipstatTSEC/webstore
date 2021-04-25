// accordian animations - start - sm

const accBtns = document.querySelectorAll('.btn')
const chevronArrow = document.querySelectorAll('.chevron')

if(innerWidth < 768) {
    const btns = [...accBtns]
    const btnsState = btns.map( btn => ({btn, closed:null}))

    for (let i = 0; i < accBtns.length; i++) {
        let panel = accBtns[i].nextElementSibling
        let childElements = Array.from(accBtns[i].children)
        btnsState[i].btn.addEventListener('click', e => {
            
            //close accordian if any other accordian is open and rotate chevron
            for (let j = 0; j < accBtns.length; j++) {
                btnsState[j].closed = false
                if(accBtns[j].nextElementSibling.classList.contains('opened')) {
                    accBtns[j].nextElementSibling.style.maxHeight = null
                    btnsState[j].closed = true
                    accBtns[j].nextElementSibling.classList.remove('opened')
                    Array.from(accBtns[j].children)[1].classList.remove("transform", "-rotate-180")
                }
            }

            //open accordian and rotate chevron
            if(btnsState[i].closed !== true){
                panel.style.maxHeight = `${panel.scrollHeight}px`;
                panel.classList.add('opened')
                childElements[1].classList.add("transition-all", "transform", "rotate-180")
            }
        })
    }
}
// accordian animations - end - sm

//accordian chevron arrows back to normal
if(innerWidth >= 768){
    chevronArrow.forEach(arrow => arrow.classList.add("transform", "-rotate-90"))
}


let dragAndDrop = function() {
    let image = document.querySelector('.includes-dd #image')

    const validFileExtensions = [...image.getAttribute('accept').split(',')]

    const browseFile = document.querySelector('.includes-dd #browse')

    browseFile.addEventListener('click', () => {
        image.click()
    })


    const uploadedImages = document.querySelector('.includes-dd .uploaded-images')

    if(innerWidth >= 768) {
        // drag and drop start
        const dropArea = document.querySelector('.includes-dd .drag-area')

        // when a file is dragging over drag-area
        dropArea.addEventListener('dragover', e => {
            e.preventDefault()
            dropArea.children[0].children[0].classList.add('animate-bounce')
            dropArea.classList.add("transition-all","border-pallete-buttonPrimary", "bg-gray-300")
        })

        // when a file dragged over drag-area was left
        dropArea.addEventListener('dragleave', e => {
            dropArea.children[0].children[0].classList.remove('animate-bounce')
            dropArea.classList.remove("border-pallete-buttonPrimary", "bg-gray-300")
        })

        let noOfImagesUploaded = 0
        // when a file is dropped in drag-area
        dropArea.addEventListener('drop', e => {
            e.preventDefault()
            dropArea.classList.remove("border-pallete-buttonPrimary", "bg-gray-300")
            dropArea.children[0].children[0].classList.remove('animate-bounce')

            let list = new DataTransfer()
            let discarded = false
            if(noOfImagesUploaded >= 5){
                alert("5 images are already uploaded.")
            }
            else{
                for(let file of e.dataTransfer.files){
                    if(noOfImagesUploaded <= 4){
                        if(validFileExtensions.includes(file.type)){
                            if(file.size <= 2097152){
                                list.items.add(file)
                                noOfImagesUploaded++
                            }
                            else
                                discarded = true
                        }else{
                            discarded = true
                        }
                    }else{
                        alert("Any five images will be taken")
                        break
                    }
                }
            }

            

            image.files = list.files
            uploadedImages.classList.remove("hidden")
            uploadedImages.classList.add("block")

            for(let photo of image.files){
                let fileReader = new FileReader()
                fileReader.onload = () => {  //this event is fired when read from file is over
                    let fileUrl = fileReader.result
                    let imgTag = `<img class="inline mr-4" src="${fileUrl}" width="50" height="50" alt="${photo.name}" title="${photo.name}">`
                    uploadedImages.innerHTML += imgTag
                }
                fileReader.readAsDataURL(photo)  //asynchronous call to read data from file
            }

            if(discarded){
                alert("Some files were discarded, either beacause they exceeded the required size limit or they were not images")
            }
        })
    }
}

dragAndDrop()