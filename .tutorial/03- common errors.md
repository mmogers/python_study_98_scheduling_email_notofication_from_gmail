# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## There's SOOOO Much

ALL of the imports have to be there!

The email settings have to be precise. Check it's the correct port & server. Check the spelling of the 'To' & 'From'.

Check that the username & password haven't been revoked. If they have, then update your secrets with the new ones.

If your code is the same as in the video, then errors on line 12 will be related to the host & port. Line 14 is username and/or password.  Line 20 or 22 is about constructing the message.

Here's one code error though:

```python
schedule.every(1).hour.do(printMe)
```

<details> <summary> 👀 Answer </summary>
  
Time intervals must be plural - `hours`, not `hour`. Even if there's only one of them.

```python
schedule.every(1).hours.do(printMe)
```

</details>

