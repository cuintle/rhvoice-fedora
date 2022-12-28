#! /usr/bin/env bash

WAYLAND_CMD="wl-paste |"
XORG_CMD="xclip -out -selection clipboard |"
SELECTION_CMD="xclip -out |"

INPUT_TYPE="clipboard"

EN_VOICE="Slt"
PTBR_VOICE="Letícia-F123"

TALKABLE_INPUT="sed 's|\btb\b|também|gI;s|\bvc\b|você|gI;s|\btd\b|tudo|gI;s|\bpq\b|porquê|gI;s|\bhj\b|hoje|gI;s|#|réchitégui- |g;s|/|-barra-|g;s|%|-porcento|g;s|@|arrôba-|g;s|gmail|gê-mê-yú|g;s|.com|-pontukôm|g' |"

HELP_MSG="""
Usage: talktext.sh [OPTIONS]
Speak copied or selected text using RHVoice

Defaults to pt_BR on Wayland.

  --pt                     Speak copied/selected text using portuguese voice
      --selection          Speaks selected text (works only on x11 sessions)
  --en                     Speak copied/selected text using english voice
      --selection          Speaks selected text (works only on x11 sessions)

  --help                   display this help and exit

Examples:
  talktext.sh --pt
  talktext.sh --en --selection
"""
function show_help() {
	echo "$HELP_MSG"
}
function force_single_proc() {
	if [ "$(ps -e | grep spd-say)" ]; then
    	killall spd-say sd_rhvoice
	fi
}

function validate_session_type() {
	[[ "$XDG_SESSION_TYPE" = "x11" ]] && SESSION_TYPE_CMD="$XORG_CMD" || SESSION_TYPE_CMD="$WAYLAND_CMD" INPUT_TYPE="clipboard"
}

function validate_selected_voice() {
	[[ "$SELECTED_LANG" = "en" ]] && SELECTED_VOICE="$EN_VOICE" || SELECTED_VOICE="$PTBR_VOICE"
}

function validate_input_type() {
	[[ "$INPUT_TYPE" = "selection" ]] && SESSION_TYPE_CMD="$SELECTION_CMD"
}
function talk() {
	TALK_CMD=""$SESSION_TYPE_CMD" "$TALKABLE_INPUT" spd-say -e -o rhvoice -y "$SELECTED_VOICE"  -r 0 -p 0 -i 10 --wait"
	eval "$TALK_CMD"
}

function main() {
	force_single_proc
	validate_session_type
	validate_selected_voice
	validate_input_type
	talk
}

while :; do
	case $1 in
	    --pt)
			SELECTED_LANG="pt"
			shift
			#TODO: Unreliable
			[[ "$1" ]] && INPUT_TYPE="selection"
			main
		    exit 0
		    ;;
	    --en)
			SELECTED_LANG="en"
			shift
			[[ "$1" ]] && INPUT_TYPE="selection"
			main
	        exit 0
			;;
		--help)
			show_help
			exit 0
			;;
		-*)
			SELECTED_LANG="pt" main
		    exit 0
		    ;;
		*)
		    SELECTED_LANG="pt" main
		    exit 0
		    ;;
	esac
done
