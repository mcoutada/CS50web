import React from 'react'

const NewPost = () => {
    return (
        <div>
        <div>
            <div id="newpost" className="row justify-content-center">
                <div class="form-group form-inline">
                    <form action="/newpost" method="post">
                        {/* {% csrf_token %} // @csrf_exempt was added in views.py so this is not needed here as jinja notation produces an error in react jsx notation */}
                        <div className="row">
                            <input className="form-control m-1" type="text" name="content" placeholder="Message"/>
                            <input className="btn btn-primary m-1" type="submit" value="Submit"/>                  
                        </div>
                    </form>
                    
                </div>  
            </div>
        </div>
        </div>
    )
}

export default NewPost
