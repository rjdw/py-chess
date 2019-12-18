package GameFoundation;
import UI.*;
import Pieces.*;

import java.awt.*;

/**
 * Created by richardwang007 on 5/18/17.
 */
import java.util.ArrayList;
public class Move {
    private Location finalLoc;
    private Piece selected;
    private Piece captured;
    private int moveValue;
    private BoardArray<Piece> board;
    private boolean playerIsWhite;
    public Move (Piece sel, Location fin, BoardArray<Piece> brd, boolean isWhite)
    {

        finalLoc = fin;
        selected = sel;
        board = brd;
        playerIsWhite = isWhite;
        captured = board.get(finalLoc);
    }

    public Piece getSelectedPiece() {
        return selected;
    }
    public Location getFinalLocation() {
        return finalLoc;
    }

    /**
     * returns the captured piece
     * @return the captured piece, null if there is no capture
     */
    public Piece getCapturedPiece() {
        return captured;
    }

    /**
     * Algebraic chess notation for the move
     * @return the algebraic chess notation
     */
    public String toString()                                                    //WORK ON PROMOTIONS AND CHECKS AND MATES LATER
    {
        String result = "";
        ArrayList<Piece> otherPossibleAttackers = new ArrayList<>();
        Location initialLoc = selected.getLocation();
        int initialLocRow = initialLoc.getRow();
        int initialLocCol = initialLoc.getCol();
        int finalLocRow = finalLoc.getRow();
        int finalLocCol = finalLoc.getCol();
        char finalCol;
        char initialCol;
        String pieceNotation = selected.getNotation();

        //ASCII conversion for the column label
        if (playerIsWhite)
        {
            finalCol = (char)(finalLocCol + 97);
            initialCol = (char)(initialLocCol + 97);
        }
        else
        {
            finalCol = (char)(104-finalLocCol);
            initialCol = (char)(104-initialLocCol);
        }

        //starts creating the string for the chess notation
        if (captured==null)
        {
            result = pieceNotation + finalCol + finalLocRow;
        }
        else {
            if (selected instanceof Pawn || selected instanceof Knight || selected instanceof Rook) {
                boolean isOtherAttacker = false;
                if (selected instanceof Pawn)
                    otherPossibleAttackers = board.getPawns();
                else if (selected instanceof Knight)
                    otherPossibleAttackers = board.getKnights();
                else if (selected instanceof Rook)
                    otherPossibleAttackers = board.getRooks();

                for (Piece other : otherPossibleAttackers)
                {
                    if (other.getColor().equals(selected.getColor()))
                    {
                        @SuppressWarnings("unchecked")
                        ArrayList<Piece> otherAttacks = other.getAttackedPiecesArray();
                        if (otherAttacks.contains(captured))
                        {
                            result = pieceNotation + initialCol + " x " + finalCol + finalLocRow;
                            isOtherAttacker = true;
                        }

                    }
                }
                if (!isOtherAttacker)
                {
                    result = pieceNotation + " x " + finalCol + finalLocRow;
                }
            }
        }

        //ADD CHECKS AND PROMOTIONS HERE


        return result;
    }

    public void setMoveValue()
    {
        int value = selected.getValue();
        //not done

    }

}
