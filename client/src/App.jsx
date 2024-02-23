import axios from 'axios';
import { useState } from 'react';

function App() {
    const BASE_API_URL = import.meta.env.VITE_BASE_API_URL;

    const [filePath, SetFilePath] = useState('');
    const [removePath, SetRemovePath] = useState('');

    const handleFileChange = (e) => {
        if (e.target.files && e.target.files[0] != undefined) {
            const f = new FormData();
            f.append('image', e.target.files[0]);
            axios
                .post(BASE_API_URL + 'upload', f)
                .then((res) => {
                    if (res.data?.success == true) {
                        SetFilePath(res.data?.data);
                    }
                })
                .catch((err) => console.log(err));
        }
    };

    const handleRemove = () => {
        axios
            .post(BASE_API_URL + `remove?filename=${filePath}`)
            .then((res) => {
                if (res?.data?.success == true) {
                    SetRemovePath(res.data?.data);
                }
            })
            .catch((err) => console.log(err));
    };

    const handleDownloadClick = () => {
        fetch(BASE_API_URL + removePath)
            .then((response) => response.blob())
            .then((blob) => {
                const url = window.URL.createObjectURL(new Blob([blob]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', removePath);
                document.body.appendChild(link);
                link.click();
                link.parentNode.removeChild(link);
            });
    };

    return (
        <>
            <div className="max-w-screen-xl mx-auto flex flex-col md:flex-row min-h-screen">
                <div className="container flex items-center justify-center w-full m-5">
                    <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                        <div className="flex flex-col items-center justify-center pt-5 pb-6">
                            <svg
                                className="w-10 h-10 mb-3 text-gray-400"
                                fill="none"
                                stroke="currentColor"
                                viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                                ></path>
                            </svg>
                            <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
                                <span className="font-semibold">
                                    Click to upload
                                </span>{' '}
                                or drag and drop
                            </p>
                            <p className="text-xs text-gray-500 dark:text-gray-400">
                                SVG, PNG, JPG or GIF
                            </p>
                        </div>
                        <input
                            onChange={handleFileChange}
                            id="dropzone-file"
                            type="file"
                            className="hidden"
                            accept="image/png image/jpg image/jpeg"
                        />
                    </label>
                </div>
                <div className="container m-5 flex flex-row h-full my-auto">
                    <div className="flex flex-col items-center h-full gap-2">
                        <img
                            src={filePath ? BASE_API_URL + filePath : ''}
                            id="upload-image"
                            className="max-h-80 max-w-80"
                        />
                        {filePath && (
                            <button
                                onClick={handleRemove}
                                className="px-4 py-2 bg-green-400 text-white rounded-md"
                            >
                                Remove Bg
                            </button>
                        )}
                    </div>
                    <div className="flex flex-col items-center h-auto justify-center gap-2">
                        <img
                            src={removePath ? BASE_API_URL + removePath : ''}
                            id="remove-image"
                            className="max-h-80 max-w-80"
                        />
                        {removePath && (
                            <button
                                className="px-4 py-2 bg-green-400 text-white rounded-md"
                                onClick={handleDownloadClick}
                            >
                                Download
                            </button>
                        )}
                    </div>
                </div>
            </div>
        </>
    );
}

export default App;
